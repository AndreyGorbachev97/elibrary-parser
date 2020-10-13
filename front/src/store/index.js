import Vue from "vue";
import Vuex from "vuex";
// import app from "../utils/axiosConfig";
import axios from "axios";
const HOST = process.env.VUE_APP_ROOT_URL;

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    data: [],
  },
  getters: {
    DATA(state) {
      return state.data;
    },
  },
  mutations: {
    SET_DATA: (state, data) => {
      state.data = data;
    },
  },
  actions: {
    GET_DATA: async (context, payload) => {
      console.log(payload);
      await axios
        .get(`${HOST}/parse`, {
          params: {
            id: payload.id,
            name: payload.name,
            startYear: payload.slider[0],
            endYear: payload.slider[1],
            directory: payload.directory,
          },
        })
        .then((res) => {
          console.log("res", res.dat);
          context.commit("SET_DATA", res.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  modules: {},
});
