<script setup>
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
    class="contact_card_container bordered"
  >
    <div>
      What is this website about? I'm not entirely sure. It's partly me learning frontend web
      development with Vue and partly a growing collection of thoughts, projects and experiences.
      <br />
      <br />
      I am currently pursuing a degree in Electrical Engineering at IIT Madaras. I am also a
      coordinator at the
      <a href="https://exploiitm.github.io" target="_blank" rel="noopener noreferrer">
        Cybersecurity</a
      >
      and the
      <a href="https://mathiitm.com" target="_blank" rel="noopener noreferrer"> Mathematics</a>
      Club at CFI IITM.
    </div>

    <div style="margin-top: 40px">
      You can reach out to me on
      <ul class="links">
        <li>
          <a href="https://github.com/swamishiju" target="_blank" rel="noopener noreferrer">
            GitHub
          </a>
          – where most of the action happens
        </li>
        <li>
          <a
            href="https://in.linkedin.com/in/swaminath-shiju-2296bb33b"
            target="_blank"
            rel="noopener noreferrer"
          >
            LinkedIn</a
          >, <a href="mailto:swaminathshiju24@gmail.com">Email</a>
          – for the professional stuff
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.contact_card_container {
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
</style>
