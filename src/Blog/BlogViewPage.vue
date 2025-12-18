<script setup>
import RegPostData from '/posts/registered.json'
import { ref, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import { Marked } from 'marked'
import { markedHighlight } from "marked-highlight";
import DOMPurify from 'dompurify'
import hljs from 'highlight.js/lib/core';
import f90 from 'highlight.js/lib/languages/fortran';
import 'highlight.js/styles/base16/black-metal-mayhem.css';
hljs.registerLanguage('f90', f90);

const route = useRoute()

const marked = new Marked(
markedHighlight({
	emptyLangClass: 'hljs',
    langPrefix: 'hljs language-',
    highlight(code, lang, info) {
      const language = hljs.getLanguage(lang) ? lang : 'plaintext';
      return hljs.highlight(code, { language }).value;
    }
  })
)

const content = ref("Loading")
watch(() => route.params.id, fetchData, { immediate: true })

async function fetchData(id) {
  const post_meta = RegPostData.registered[id];

  if (post_meta == null) {
    content.value = computed(() => "Page doesn't exist")
  } else {
    const post_fetch = await fetch(`/${post_meta.path}`)
    if (post_fetch.ok === true) {
      let post = await post_fetch.json()
      content.value = computed(() => DOMPurify.sanitize(marked.parse(post.content)))
    }
  }

  console.log(content.value)
}

const props = defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
})

const fontSize = () => (props.CollapseSidebar ? 2.6 : 1.3)
</script>

<template>
  <div
    :class="{ left_shift: !CollapseSidebar, top_shift: CollapseSidebar }"
    class="bordered blog_container"
  >
    <div class="content_item" v-html="content.value"></div>
  </div>
</template>

<style scoped>
.blog_container {
  padding: 20px 6vw 0 20px;
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

.link {
  color: #fff;
  text-decoration: none;
  border-bottom: 1px solid #555;
  padding-bottom: 2px;
  transition: all 0.2s ease;
}

.link:hover,
.link:focus {
  color: #aaa;
  border-bottom-color: #aaa;
}
</style>
