<script setup>
defineProps({
  external: {
    type: Boolean,
    default: false,
  },
  PathEx: {
    type: String,
    default: '',
  },
  PathIn: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <a v-if="external" :href="PathEx" target="_blank" rel="noopener noreferrer">
    <slot />
  </a>
  <RouterLink v-else :to="PathIn">
    <slot />
  </RouterLink>
</template>

<style scoped>
a {
  all: unset;
  text-decoration: none;
  color: inherit;
}
</style>
