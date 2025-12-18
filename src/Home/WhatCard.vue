<script setup>
import { GraduationCap, Folder, AppWindow, Gitlab, Pi, Microchip, Cpu, Cat } from 'lucide-vue-next'

const props = defineProps({
  CollapseSidebar: {
    type: Boolean,
    default: false,
  },
})
const fontSize = () => (props.CollapseSidebar ? 1.7 : 1.1)
</script>

<template>
  <div class="what_card_container bordered" :class="{ left_shift: !CollapseSidebar }">
    <p class="c3">
      <span class="c0">[ </span>
      <span class="c1">d4pr0</span>@<span class="c5">archlinux</span>
      <span class="c0"> ]</span>
      whoami
      <br />
      Hey, I'm
      <span class="c6">Swaminath Shiju</span>
      <br />
      You can find me online as
      <span class="c2">swamishiju</span>
      or
      <span class="c2">d4pr0</span>
      <br />
      <span class="c0">[ </span>
      <span class="c1">d4pr0</span>@<span class="c5">archlinux</span>
      <span class="c0"> ]</span>
      ./what_i_do.sh
      <br />
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <span class="c7">.</span
      >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <span class="c1">d4pr0</span>@<span class="c5">archlinux</span>
      <br />
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      -------------------------------------------
      <br />
      <span class="c6">
        <b
          >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c7">*</span>&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">,MMM8&amp;&amp;</span
          >&amp;.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c7">*</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >[<span class="icon-container"><GraduationCap class="icon" /></span>]</span
          >
          <span class="c3">
            I am a <span class="c5">Sophomore</span> at <span class="c6">IIT Madras</span></span
          ><br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">MMM<span class="c3">M8</span>8M&amp;&amp;&amp;</span
          >&amp;&amp;&nbsp;&nbsp;&nbsp; <span class="c7">.</span>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c3"> majoring in <span class="c6">Electrical Engineering</span> </span><br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">MMM<span class="c3">M88&amp;</span>&amp;&amp;&amp;</span
          >&amp;&amp;&amp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >[<span class="icon-container"><Folder class="icon" /></span>]</span
          >
          <span class="c3"> Fun stuff I like</span>
          <br />
          &nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c7">*</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">MMM88<span class="c3">&amp;&amp;&amp;</span>&amp;&amp;&amp;</span
          >&amp;&amp;&amp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >├──[<span class="icon-container"><Gitlab class="icon" /></span>]</span
          >
          Open Source Developement<br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">MMM88&amp;&amp;&amp;&amp;</span
          >&amp;&amp;&amp;&amp;&amp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >├──[<span class="icon-container"><AppWindow class="icon" /></span>]</span
          >
          CTFs<br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">'MMM88&amp;&amp;</span
          >&amp;&amp;&amp;&amp;&amp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >├──[<span class="icon-container"><Pi class="icon" /></span>]</span
          >
          Higher Mathematics<br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          'MMM8&amp;&amp;&amp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c7">*</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >├──[<span class="icon-container"><Microchip class="icon" /></span>]</span
          >
          Embedded Development<br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="c1">|\___/|</span>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >├──[<span class="icon-container"><Cpu class="icon" /></span>]</span
          >
          Kernel Development<br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c1">)&nbsp;&nbsp;&nbsp;&nbsp; (</span
          >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c7">.</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c7"
            >'</span
          >
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c0"
            >└──[<span class="icon-container"><Cat class="icon" /></span>]</span
          >
          Cats<br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c4">=</span><span class="c1">\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/</span><wbr />
          <span class="c4">=</span><br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c1">)</span><span class="c0">===</span
          ><span class="c1">(</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="c7">*</span
          ><br />
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <span class="c1"
            >/&nbsp;&nbsp;&nbsp;&nbsp; \<br />
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |&nbsp;&nbsp;&nbsp;&nbsp; |<br />
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            \</span
          >
        </b>
      </span>
    </p>
  </div>
</template>

<style scoped>
.what_card_container {
  padding-left: 20px;
  margin: 0 5px 5px 5px;
  background: #000;
  opacity: 80%;
  color: #bbb;
  font-family: 'JetBrains Mono', monospace;
  box-sizing: border-box;
  position: fixed;
  inset: 30vh 0 0 0;

  display: grid;
  place-items: baseline;
  font-size: v-bind(fontSize() + 'vw');
}

.icon {
  width: 3vh;
  height: 1.5vw;
  color: rgb(252, 237, 68);
}

.icon-container {
  display: inline-flex;
  align-items: center;
}

.c0 {
  color: rgb(79, 117, 117);
}
.c1 {
  color: rgb(211, 133, 136);
}
.c2 {
  color: rgb(143, 82, 83);
}
.c3 {
  color: rgb(117, 117, 117);
}
.c4 {
  color: rgb(136, 136, 136);
}
.c5 {
  color: rgb(154, 154, 154);
}
.c6 {
  color: rgb(180, 180, 180);
}
.c7 {
  color: rgb(252, 237, 68);
}
</style>
