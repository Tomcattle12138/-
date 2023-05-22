<template>
  <div>
    <div id="title_div">预测对比展示</div>
    <plot
      v-for="(graph, index) in graphs"
      :width="12"
      :key="index"
      :title="titles[index]"
      :date="graph.date"
      :high="graph.high"
      :low="graph.low"
      :open="graph.open"
      :close="graph.close"
    >
    </plot>
  </div>
</template>

<script>
import Plot from "../Utils/Plot.vue";
import axios from "axios";

export default {
  data() {
    return {
      graphs: [],
      titles: [],
    };
  },
  components: {
    Plot,
  },
  mounted() {
    this.get_showfinishwork();
  },
  methods: {
    get_showfinishwork() {
      var that = this;
      axios.get("/api/medium_regression/showfinishwork").then(
        (res) => {
          res = res.data;
          var graph_cnts = res.graph_cnts;
          var generate_graphs = res.generate;
          var real_graphs = res.real;
          for (var i = 0; i < graph_cnts; ++i) {
            that.titles.push(real_graphs[i].year_month + "真实汇率");
            that.titles.push(generate_graphs[i].year_month + "预测汇率");
            that.graphs.push(real_graphs[i]);
            that.graphs.push(generate_graphs[i]);
          }
        },
        (error) => {
          alert("请求数据发生错误");
        }
      );
    },
  },
};
</script>

<style scoped>
#title_div {
  text-align: center;
  font-size: 35px;
  font-family: 方正书宋体;
  font-weight: bold;
}
</style>