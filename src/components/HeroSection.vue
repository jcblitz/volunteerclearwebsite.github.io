<script setup lang="ts">
import CTAButton from './CTAButton.vue';
</script>

<template>
  <section
    id="hero"
    class="relative min-h-screen flex items-center justify-center overflow-hidden"
    style="background: linear-gradient(to bottom right, #2563eb, #1d4ed8, #7c3aed);"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute inset-0" style="background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 40px 40px;"></div>
    </div>

    <!-- Content -->
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
      <div class="animate-fade-in-up">
        <h1 class="text-4xl sm:text-5xl md:text-6xl font-bold text-white mb-6 leading-tight">
          Keep Kids Safe. Stay Compliant.<br />
          Simplify Volunteer Management.
        </h1>
        <p class="text-xl sm:text-2xl mb-10 max-w-3xl mx-auto" style="color: rgba(255, 255, 255, 0.9);">
          Secure platform for volunteers & organizations to manage clearances & background checks all in one place.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <CTAButton
            text="Start Free Trial"
            variant="secondary"
            size="lg"
            href="https://app.volunteerclear.com/login"
          />
          <CTAButton
            text="Watch Demo"
            variant="outline"
            size="lg"
            href="#features"
          />
        </div>
      </div>
    </div>

    <!-- Scroll Indicator -->
    <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
      <svg
        class="w-6 h-6 text-white"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 14l-7 7m0 0l-7-7m7 7V3"
        />
      </svg>
    </div>
  </section>
</template>

<style scoped>
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out;
}
</style>
