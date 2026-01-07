<script setup lang="ts">
import { EnvelopeIcon } from '@heroicons/vue/24/outline';
import CTAButton from './CTAButton.vue';
</script>

<template>
  <section id="contact" class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
          Get in Touch
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Ready to get started? Sign up for free or reach out to us directly with any questions.
        </p>
      </div>

      <div class="max-w-2xl mx-auto">
        <!-- Call to Action -->
        <div class="text-center mb-12">
          <CTAButton
            text="Start Free Trial"
            variant="primary"
            size="lg"
            href="https://app.volunteerclear.com/register"
            target="_blank"
            class="mb-4"
          />
          <p class="text-gray-600">
            No credit card required • Free during early access
          </p>
        </div>

        <!-- Contact Information -->
        <div class="bg-white rounded-lg p-8 shadow-sm text-center">
          <div class="flex justify-center mb-4">
            <EnvelopeIcon class="h-8 w-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold text-gray-900 mb-2">Questions?</h3>
          <p class="text-gray-600 mb-4">
            We'd love to hear from you. Send us an email and we'll respond within 24 hours.
          </p>
          <a
            href="mailto:hello@volunteerclear.com"
            class="inline-flex items-center text-lg font-semibold text-primary-600 hover:text-primary-700 transition-colors"
          >
            hello@volunteerclear.com
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
