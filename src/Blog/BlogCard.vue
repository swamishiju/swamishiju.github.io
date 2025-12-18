<script setup>
import { Calendar } from 'lucide-vue-next'
import { marked } from 'marked'
import DOMPurify from 'dompurify'
import RegPostData from '/posts/registered.json'
import { computed } from 'vue'
import UtilLink from '../Utils/UtilLink.vue'

const props = defineProps({
  PostId: {
    type: String,
    default: '',
  },
})
const post_meta = RegPostData.registered[props.PostId] ?? {
  title: 'Error loading card',
  date: 'Jan 1, 1970',
  tags: ['Error'],
  abstract: ':(',
}

const post_abstract = computed(() => DOMPurify.sanitize(marked.parse(post_meta['abstract'])))
</script>

<template>
  <UtilLink :external="post_meta.external" :PathEx="post_meta.path" :PathIn="'blog/' + PostId">
    <div class="blog_card bordered">
      <div class="blog_card_header">
        <div class="title_item">{{ post_meta.title }}</div>
        <div class="date_item"><Calendar size="12" /> {{ post_meta.date }}</div>
      </div>
      <div class="content_item" v-html="post_abstract"></div>
      <div class="blog_card_footer">
        <div class="bordered tag" v-for="tag in post_meta.tags" :key="tag">
          {{ tag }}
        </div>
      </div>
    </div></UtilLink
  >
</template>

<style scoped>
.blog_card {
  background: #000;
  opacity: 90%;
  color: #bbb;
  margin: 5px;
  position: relative;
}

.content_item {
  padding: 20px 20px 20px 20px;
}

.date_item {
  padding: 10px 20px;
  font-family: 'Roboto Mono', monospace;
  display: flex;
  align-items: center;
  gap: 10px;
}

.title_item {
  padding: 10px;
  flex-grow: 1;
  border-right: inherit;
  margin: 0;
  color: #eee;
}

.blog_card_header {
  display: flex;
  flex-direction: row;
  padding: 0;
  border: inherit;
  border-top-right-radius: inherit;
  border-top-left-radius: inherit;
  margin: -1px;
}

.blog_card_footer {
  display: flex;
  flex-direction: row;
  padding: 0;
  border: inherit;
  border-bottom-right-radius: inherit;
  border-bottom-left-radius: inherit;
  margin: -1px;
}

.tag {
  margin: 8px 8px;
  padding: 4px 8px;
  font-family: 'Roboto Mono', monospace;
  display: flex;
  align-items: center;
  font-size: 12px;
}
</style>
