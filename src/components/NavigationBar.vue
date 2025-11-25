<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline';
import CTAButton from './CTAButton.vue';

const isScrolled = ref(false);
const isMobileMenuOpen = ref(false);

const navLinks = [
  { name: 'Home', href: '#hero' },
  { name: 'Features', href: '#features' },
  { name: 'Pricing', href: '#pricing' },
  { name: 'Blog', href: '/blog/', external: true },
  { name: 'Contact', href: '#contact' },
];

const handleScroll = () => {
  isScrolled.value = window.scrollY > 20;
};

const scrollToSection = (href: string) => {
  const element = document.querySelector(href);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
    isMobileMenuOpen.value = false;
  }
};

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<template>
  <nav
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-300',
      isScrolled ? 'bg-white shadow-md' : 'bg-transparent',
    ]"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="flex-shrink-0">
          <a
            href="#hero"
            :class="[
              'text-2xl font-bold transition-colors',
              isScrolled ? 'text-primary-600' : 'text-white',
            ]"
            @click.prevent="scrollToSection('#hero')"
          >
            VolunteerClear
          </a>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <a
            v-for="link in navLinks"
            :key="link.name"
            :href="link.href"
            :class="[
              'font-medium transition-colors hover:text-primary-600',
              isScrolled ? 'text-gray-700' : 'text-white',
            ]"
            @click="(e) => { if (!link.external) { e.preventDefault(); scrollToSection(link.href); } }"
          >
            {{ link.name }}
          </a>
          <CTAButton
            text="Get Started"
            variant="primary"
            size="sm"
            href="#contact"
            @click="scrollToSection('#contact')"
          />
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button
            type="button"
            :class="[
              'p-2 rounded-md transition-colors',
              isScrolled ? 'text-gray-700 hover:bg-gray-100' : 'text-white hover:bg-white/10',
            ]"
            :aria-label="isMobileMenuOpen ? 'Close menu' : 'Open menu'"
            :aria-expanded="isMobileMenuOpen"
            @click="toggleMobileMenu"
          >
            <Bars3Icon v-if="!isMobileMenuOpen" class="h-6 w-6" />
            <XMarkIcon v-else class="h-6 w-6" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-1"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-1"
    >
      <div
        v-if="isMobileMenuOpen"
        class="md:hidden bg-white border-t border-gray-200"
      >
        <div class="px-4 pt-2 pb-3 space-y-1">
          <a
            v-for="link in navLinks"
            :key="link.name"
            :href="link.href"
            class="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-primary-600 hover:bg-gray-50"
            @click="(e) => { if (!link.external) { e.preventDefault(); scrollToSection(link.href); } }"
          >
            {{ link.name }}
          </a>
          <div class="pt-2">
            <CTAButton
              text="Get Started"
              variant="primary"
              size="md"
              href="#contact"
              class="w-full"
              @click="scrollToSection('#contact')"
            />
          </div>
        </div>
      </div>
    </Transition>
  </nav>
</template>
