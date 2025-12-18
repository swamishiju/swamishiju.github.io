<script setup>
import { reactive, ref } from 'vue'
import SideBarItem from './SideBarItem.vue'
import { Home, FolderGit2, Mail, Notebook, Menu } from 'lucide-vue-next'

const sidebar = reactive({
  items: [
    { id: 1, route: '/', text: 'HOME', icon: Home },
    { id: 2, route: '/projects', text: 'PROJECTS', icon: FolderGit2 },
    { id: 3, route: '/blog', text: 'BLOG', icon: Notebook },
    { id: 4, route: '/about', text: 'ABOUT', icon: Mail },
  ],
})

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

</script>

<template>
  <nav v-if="!CollapseSidebar || togglebar" class="sidebar bordered" @click="toggle">
    <ul>
      <li v-for="item in sidebar.items" :key="item.id">
        <SideBarItem :icon="item.icon" :route="item.route">{{ item.text }}</SideBarItem>
      </li>
    </ul>
  </nav>
  <Menu v-if="CollapseSidebar" class="menu bordered" @click="toggle" />
</template>

<style scoped>
.sidebar {
  position: fixed;
  inset-block: 0;
  inset-inline-start: 0;
  width: 280px;
  padding: 20px 5px 20px 5px;
  margin: 5px;
  background: #000;
  color: #bbb;
  font-family: 'Roboto', sans-serif;
  box-sizing: border-box;
  z-index: 1;
  overflow-x: hidden;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

li + li {
  margin-top: 8px;
}

.menu {
  position: fixed;
  z-index: 1;
  color: #eee;
  padding: 5px;
  margin: 5px;
  background-color: #000;
  border-color: rgb(104, 57, 57);
}
</style>
