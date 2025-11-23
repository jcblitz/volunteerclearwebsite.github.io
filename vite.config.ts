import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    // Enable minification
    minify: true,
    // Code splitting
    rollupOptions: {
      output: {
        manualChunks: {
          'vendor': ['vue'],
          'heroicons': ['@heroicons/vue/24/outline', '@heroicons/vue/24/solid'],
        },
      },
    },
    // Chunk size warnings
    chunkSizeWarningLimit: 1000,
  },
  // SEO-friendly base URL
  base: '/',
})
