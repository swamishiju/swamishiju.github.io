<script setup>
const props = defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
})

const fontSize = () => (props.CollapseSidebar ? 6.5 : 3.5)
</script>

<template>
  <div
    :class="{ left_shift: !CollapseSidebar, top_shift: CollapseSidebar }"
    class="name_card_container bordered"
  >
    <div class="name_card"><span class="color">Hey</span>,I'm Swaminath Shiju</div>
  </div>
</template>

<style scoped>
.name_card_container {
  padding: 20px 5px 20px 5px;
  margin: 5px;
  background: #000;
  opacity: 67%;
  color: #bbb;
  font-family: 'Roboto Mono', monospace;
  box-sizing: border-box;
  position: fixed;
  inset: 0 0 70vh 0;

  display: grid;
  place-items: center;
  font-size: v-bind(fontSize() + 'vw');
}

.name_card {
  padding: 10px;
  text-align: center;
}

.color {
  color: #83535c;
}
</style>
