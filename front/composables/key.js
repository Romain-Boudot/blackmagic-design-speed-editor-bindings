import {useState} from "#app";

const commands = [17, 18, 16, 91, 93]

const onKeyDown = (callback) => {
  return function (e) {
    e.preventDefault()
    e.stopPropagation()
    if (commands.includes(e.keyCode)) {
      return false
    }
    const key = e.key === ' ' ? 'space' : e.key.toLowerCase()
    callback(`${e.metaKey ? 'cmd+' : ''}${e.ctrlKey ? 'ctrl+' : ''}${e.altKey ? 'alt+' : ''}${e.shiftKey ? 'shift+' : ''}${key}`)
    return false
  }
}

export function useGetBinding(code) {
  return useState(code, () => '')
}

export function useSetBinding(code, binding) {
  const bind = useState(code)
  bind.value = binding
  const form = new FormData()
  form.set('binding', binding)
  return fetch(`http://localhost:5005/api/keys/${code}`, {
    method: 'POST',
    body: form,
  })
}

export function useGatherAllBindings() {
  fetch('http://localhost:5005/api/keys').then((response) => {
    response.json().then((data) => {
      Object.entries(data).forEach(([code, value]) => {
        const bind = useState(code)
        bind.value = value
        console.log(code, value)
      })
    })
  }).catch((error) => {
    console.error(error)
  })
}

export function useListenKey() {
  return new Promise((resolve) => {
    const listener = onKeyDown(function (binding){
      resolve(binding)
      window.removeEventListener('keydown', listener)
    })
    window.addEventListener('keydown', listener)
  })
}
