<script setup>
import UtilLink from '../Utils/UtilLink.vue'

defineProps({
  icon: {
    type: Function,
    default: null,
  },
  route: {
    type: String,
    default: null,
  },
})
</script>

<template>
  <UtilLink :external="false" :PathIn="route">
    <div class="item bordered_item" :class="{ active: $route.fullPath == route }">
      <component v-if="icon" :is="icon" size="12" />
      <span><slot>Empty Item</slot></span>
    </div>
  </UtilLink>
</template>

<style scoped>
.item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 10px;
  background-color: #020202;
  margin: 6px 25px;
  text-align: center;

  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.item:hover {
  color: #eee;
  background-color: #000;
  transform: translateY(-3px);
}

.active {
  color: #eee;
}

.bordered_item {
  border-width: thin;
  border-radius: 5px;
  border-style: solid hidden solid hidden;
  border-color: rgb(28, 7, 7);
}

.bordered_item:hover {
  border-color: rgb(104, 57, 57);
}
</style>
