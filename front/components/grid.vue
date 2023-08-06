<template>
  <div class="grid" :style="{
    gridTemplateColumns: `repeat(${cols * 2}, 45px)`,
    gridTemplateRows: `repeat(${rows * 2}, 45px)`
  }">
    <slot />
  </div>
</template>

<script setup>
defineProps(['cols', 'rows', 'keysize'])
</script>

<style>
.grid {
  display: grid;
  gap: 5px;
}
</style>
