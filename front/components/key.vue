<template>
  <div @click="handleClick" class="key" :class="{ listening }" :style="{
    gridColumnStart: 'span ' + (width || 1) * 2,
    gridRowStart: 'span 2',
    backgroundColor: color,
    '--color': color,
    color: color === 'white' ? 'black' : 'white',
    border: color === 'white' ? '1px solid black' : 'none',
    cursor: disabled ? 'not-allowed' : 'pointer'
  }">
    <div>{{ binding }}</div>
  </div>
</template>

<script setup>
const props = defineProps(['color', 'width', 'name', 'code', 'disabled'])

const listening = ref(false)
const code = parseInt(props.code).toString()
const binding = useGetBinding(code)

function handleClick() {
  if (props.disabled) return
  listening.value = true
  useListenKey()
    .then((binding) => {
      listening.value = false
      useSetBinding(code, binding)
    })
}

</script>

<style>
.key {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 0.8rem;
  border-radius: 5px;
  font-family: "Helvetica Neue", sans-serif;
  cursor: pointer;
  text-align: center;
  padding: 5px;
  --color: white;
}

@keyframes outlineAnimation {
  0% {
    outline: 2px solid var(--color);
  }
  50% {
    outline: 2px solid blue;
  }
  100% {
    outline: 2px solid var(--color);
  }
}

.key.listening {
  animation: outlineAnimation 2s infinite;
}
</style>
