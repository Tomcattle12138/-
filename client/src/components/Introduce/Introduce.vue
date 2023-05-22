<template>
  <div>
    <el-row class="tac">
      <side-bar :menus="menus" :link="link"></side-bar>
      <el-col :span="18" :offset="2">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import SideBar from "@/components/Utils/SideBar.vue"
Vue.use(ElementUI);

export default {
  components: {
    SideBar,
  },
  data() {
    return {
      menus: ['数据集介绍', '数据集可视化'],
      link: ['/introduce/dataset_introduce', '/introduce/dataset_visible']
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
