<template>
    <div id="app">
        <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
            <el-menu-item index="1" :span="6"><router-link to="/introduce"> 项目介绍  </router-link></el-menu-item>
            <el-menu-item index="2" :span="6"><router-link to="/medium_regression"> 中期回归 </router-link></el-menu-item>
            <el-menu-item index="3" :span="6">长期回归</el-menu-item>
            <el-menu-item index="4" :span="6">聚类分析</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)
export default {
    name: 'NavigatorBar',
    data() {
        return {
            activeIndex: '1',
            activeIndex2: '1'
        };
    },
    methods: {
        handleSelect(key, keyPath) {
            //console.log(key, keyPath);
        }
    }
}
</script>

<style scoped>
    a {
    text-decoration: none;
    }
</style>
