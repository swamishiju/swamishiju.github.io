<script setup>
import NameCard from './NameCard.vue'
import WhatCard from './WhatCard.vue'

defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <NameCard :CollapseSidebar="CollapseSidebar" />
  <WhatCard :CollapseSidebar="CollapseSidebar" />
</template>
