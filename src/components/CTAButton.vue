<script setup lang="ts">
import type { CTAButtonProps } from '../types/marketing';

const props = withDefaults(defineProps<CTAButtonProps>(), {
  variant: 'primary',
  size: 'md',
});

const emit = defineEmits<{
  click: [];
}>();

const getVariantStyles = () => {
  switch (props.variant) {
    case 'primary':
      return {
        backgroundColor: '#2563eb',
        color: 'white',
        border: 'none',
      };
    case 'secondary':
      return {
        backgroundColor: 'white',
        color: '#2563eb',
        border: 'none',
      };
    case 'outline':
      return {
        backgroundColor: 'transparent',
        color: 'white',
        border: '2px solid white',
      };
    default:
      return {};
  }
};

const sizeClasses = {
  sm: 'px-4 py-2 text-sm',
  md: 'px-6 py-3 text-base',
  lg: 'px-8 py-4 text-lg',
};

const handleClick = () => {
  emit('click');
};
</script>

<template>
  <component
    :is="href ? 'a' : 'button'"
    :href="href"
    :target="target"
    :style="getVariantStyles()"
    :class="[
      'inline-flex items-center justify-center font-semibold rounded-lg transition-all duration-200',
      'focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white',
      'hover:opacity-90',
      sizeClasses[size],
    ]"
    @click="handleClick"
  >
    {{ text }}
  </component>
</template>
