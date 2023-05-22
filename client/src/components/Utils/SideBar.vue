<template>
    <div>
        <el-col :span="4">
            <h5>功能选项</h5>
            <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
                <el-menu-item v-for="menu, idx in menus" :key="idx">
                    <i class="el-icon-menu"></i>
                    <span slot="title"><router-link :to="link[idx]">{{ menu }}</router-link></span>
                </el-menu-item>
            </el-menu>
        </el-col>
    </div>
</template>
  
<script>
import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
Vue.use(ElementUI);

export default {
    props: {
        menus: {
            type: Array,
            default: () => []
        },
        link: {
            type: Array,
            default: () => []
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
  