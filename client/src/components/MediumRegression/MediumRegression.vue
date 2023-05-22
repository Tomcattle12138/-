<template>
  <div>
    <el-row class="tac">
      <side-bar :menus="menus" :link="link"></side-bar>
      <el-col :span="20">
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
      menus: ['作品展示', '在线测试'],
      link: ['/medium_regression/show_finishwork', '/medium_regression/test_online']
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
