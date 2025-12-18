<script setup>
import BlogSideBar from './BlogSideBar/BlogSideBar.vue'
import BlogCard from './BlogCard.vue'
import { Search } from 'lucide-vue-next'
import { ref } from 'vue'
const props = defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
})

const togglebar = ref(false)
const toggle = () => {
  togglebar.value = !togglebar.value
}


import PostData from '/posts/registered.json'
const fontSize = () => (props.CollapseSidebar ? 2.6 : 1.3)
</script>

<template>
  <div :class="{ left_shift: !CollapseSidebar, top_shift: CollapseSidebar }" class="blog_container">
    <div class="blog_card_container">
      <BlogCard v-for="post in PostData.listed" :PostId="post" :key="post" />
    </div>
    <BlogSideBar :CollapseSidebar="CollapseSidebar" :togglebar="togglebar"/>
  </div>
  <Search v-if="CollapseSidebar" class="search bordered" @click="toggle"/>
</template>

<style scoped>
.blog_container {
  position: fixed;
  inset: 0 0 0 0;
  font-family: 'Roboto', sans-serif;
  box-sizing: border-box;

  display: flex;
  flex-direction: row;
  font-size: v-bind(fontSize() + 'vw');
  overflow-y: scroll;
}

.blog_card_container {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.search {
  position: fixed;
  z-index: 1;
  color: #eee;
  padding: 5px;
  margin: 5px;
  background-color: #000;
  border-color: rgb(104, 57, 57);
  right: 0;
}
</style>
