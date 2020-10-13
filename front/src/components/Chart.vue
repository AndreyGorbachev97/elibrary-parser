<template>
  <div style="height: 60vh;">
    <canvas ref="canvas"></canvas>
  </div>
</template>

<script>
import { Line, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

export default {
  name: "Chart",
  mixins: [reactiveProp],
  props: ["options"],
  extends: Line,
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
  data() {
    return {};
  }
};
</script>

<style lang="scss" scoped>
</style>
