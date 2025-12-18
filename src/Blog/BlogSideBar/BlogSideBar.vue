<script setup>
import { reactive, ref } from 'vue'
import SideBarItem from './BlogSideBarItem.vue'
import {Search} from 'lucide-vue-next'

const sidebar = reactive({
  items: [
    { id: 1, text: 'Filter by tag' },
    // { id: 2, text: 'PROJECTS'},
    // { id: 3, text: 'BLOG', icon: Notebook },
    // { id: 4, text: 'ABOUT', icon: Mail },
  ],
})

defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
  togglebar: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <nav v-if="!CollapseSidebar || togglebar" class="sidebar bordered">
    <ul>
      <li v-for="item in sidebar.items" :key="item.id">
        <SideBarItem>{{ item.text }}</SideBarItem>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.sidebar {
  padding: 20px 5px 20px 5px;
  margin: 5px;
  background: #000;
  color: #bbb;
  font-family: 'Roboto', sans-serif;
  font-size: 15px;
  box-sizing: border-box;
  z-index: 1;
  width: 30vw;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

/* Optional: nice spacing for items */
li + li {
  margin-top: 8px;
}
</style>
