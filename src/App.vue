<script setup>
import SideBar from './SideBar/SideBar.vue'
import { ref, onMounted, onUnmounted } from 'vue'
const CollapseSidebar = ref(false)

// Collapse automatically below 768px (md breakpoint)
const checkWidth = () => {
  const shouldCollapse = window.innerWidth < 768
  if (shouldCollapse && !CollapseSidebar.value) {
    CollapseSidebar.value = true
  } else if (!shouldCollapse && CollapseSidebar.value) {
    CollapseSidebar.value = false
  }
}

onMounted(() => {
  checkWidth()
  window.addEventListener('resize', checkWidth)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkWidth)
})
</script>

<template>
  <SideBar :CollapseSidebar="CollapseSidebar" />
  <RouterView v-slot="{ Component }">
    <component :is="Component" :CollapseSidebar="CollapseSidebar" />
  </RouterView>
</template>

<style>
body {
  margin: 0;
  background-color: #080808;
  background-image: url('https://raw.githubusercontent.com/dharmx/walls/refs/heads/main/monochrome/a_street_lights_at_night_01.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  min-height: 100vh;
}

.bordered {
  border-width: thin;
  border-radius: 10px;
  border-style: solid;
  border-color: hsl(0, 60%, 20%);

  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.bordered:hover {
  border-color: hsl(0, 60%, 60%);
  opacity: 100%;
}

.left_shift {
  margin-left: 290px !important;
}

.top_shift {
  margin-top: 45px !important;
}

a {
  color: #fff;
  text-decoration: none;
  border-bottom: 1px solid #555;
  transition: all 0.2s ease;
}

a:hover,
a:focus {
  color: #aaa;
  border-bottom-color: #aaa;
}
</style>
