<template>
  <v-app>
    <app-bar />
    <v-content>
      <div class="main">
        <div style="width: 27vw">
          <v-range-slider
            hint
            v-model="slider"
            thumb-label="always"
            min="2000"
            max="2020"
            ticks
            tick-size="4"
          ></v-range-slider>
          <v-text-field v-model="id" rounded filled placeholder="id" dense></v-text-field>
          <v-text-field v-model="name" rounded filled placeholder="имя файла" dense></v-text-field>
          <v-text-field v-model="directory" rounded filled placeholder="директория для файла" dense></v-text-field>
          <div>
            <v-btn
              style="width: 100%"
              class="mr-2 mt-2"
              small
              color="primary"
              @click="generateChart()"
            >сформировать файл</v-btn>
          </div>
        </div>
        <div style="width: 60vw; margin-left: 5%; margin-top: -30px">
          <chart v-if="chartData && !progress" :chart-data="chartData" :options="options" />
          <div v-if="progress === true" class="message">
            <v-progress-circular :size="70" :width="7" color="primary" indeterminate></v-progress-circular>
          </div>
          <div v-if="inf" class="message">
            <div class="message-block">
              <div style="display: flex; justify-content: center;">сформируйте файл</div>
              <div>для отображения статистики</div>
            </div>
          </div>
        </div>
      </div>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AppBar from "./components/AppBar.vue";
import Chart from "./components/Chart.vue";

export default {
  name: "App",
  components: {
    AppBar,
    Chart
  },
  computed: mapGetters(["DATA"]),
  methods: {
    ...mapActions(["GET_DATA"]),
    async generateChart() {
      this.progress = true;
      await this.GET_DATA({
        name: this.name,
        id: this.id,
        directory: this.directory,
        slider: this.slider
      });
      this.progress = false;
      this.inf = false;
      console.log(this.DATA);
      const yearSlice = this.year.slice(
        this.year.indexOf(this.slider[0]),
        this.year.indexOf(this.slider[1]) + 1
      );
      console.log(yearSlice);
      this.chartData = {
        labels: yearSlice,
        datasets: [
          {
            label: "Статьи",
            backgroundColor: "#F44336",
            borderColor: "#F44336",
            data: yearSlice.reduce((acc, el) => {
              let temp = [...this.DATA].filter(_ => _.year === el.toString())
                .length;
              acc = [...acc, temp];
              return acc;
            }, []),
            // borderDash: [10,5],
            fill: false
          }
        ]
      };
    }
  },
  data: () => ({
    inf: true,
    name: "",
    progress: false,
    id: "736901",
    directory: "C:/docs/",
    slider: [2008, 2020],
    thisYear: Number(new Date().getFullYear()),
    year: Array.apply(null, { length: 21 }).map(
      (el, i) => Number(new Date().getFullYear()) - 20 + i
    ),
    chartData: null,
    options: {
      responsive: true,
      legend: {
        position: "top"
      },
      title: {
        display: true
      }
    }
  })
};
</script>

<style scoped>
.main {
  display: flex;
  margin: 4% 5%;
}
.message {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60vh;
  font-size: 24px;
  color: #a5a5a5;
}
.message-block {
  display: flex;
  flex-direction: column;
}
</style>
