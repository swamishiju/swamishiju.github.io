<script setup>
import { ref } from 'vue'
import { marked } from 'marked'
import DOMPurify from 'dompurify'

import listMarkdown from './list.md?raw'

const props = defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
})

const fontSize = () => (props.CollapseSidebar ? 2.6 : 1.3)
const listHtml = ref(DOMPurify.sanitize(marked(listMarkdown)));
</script>

<template>
  <div
    :class="{ left_shift: !CollapseSidebar, top_shift: CollapseSidebar }"
    class="media_card_container bordered"
  >
  This a growing, non-exhaustive list of stuff I think are cool and want to read/watch sometime
  <br/>

    <div v-html="listHtml"> </div>
  </div>
</template>

<style scoped>
.media_card_container {
  padding: 20px 0 0 20px;
  margin: 5px;
  background: #000;
  opacity: 80%;
  color: #bbb;
  font-family: 'Roboto Mono', monospace;
  box-sizing: border-box;
  position: fixed;
  inset: 0 0 0 0;

  display: flex;
  flex-direction: column;
  font-size: v-bind(fontSize() + 'vw');
  overflow-y: scroll;
}

.links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.links li {
  margin: 0;
}

.media_card_container :deep(em) {
  opacity: 0.5;
}
</style>
