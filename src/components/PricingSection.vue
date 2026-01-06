<script setup lang="ts">
import { CheckIcon } from '@heroicons/vue/24/solid';
import CTAButton from './CTAButton.vue';
import type { PricingTier } from '../types/marketing';

const pricingTiers: PricingTier[] = [
  {
    id: 'solo',
    name: 'Solo',
    price: 'Free',
    period: 'during early access',
    description: 'Perfect for small organizations just getting started',
    features: [
      'Up to 10 volunteers',
      '1 organization',
      'All core features',
      'Document upload & storage',
      'Compliance dashboard',
      'Email support',
    ],
    cta: 'Sign Up Free',
    ctaLink: 'https://app.volunteerclear.com/login',
    highlighted: false,
  },
  {
    id: 'team',
    name: 'Team',
    price: 'Free',
    period: 'during early access',
    description: 'Best for growing organizations with more volunteers',
    features: [
      'Up to 50 volunteers',
      '1 organization',
      'All features',
      'Custom clearance types',
      'Expiration alerts',
      'Priority support',
      'Advanced reporting',
    ],
    cta: 'Sign Up Free',
    ctaLink: 'https://app.volunteerclear.com/login',
    highlighted: true,
  },
  {
    id: 'program',
    name: 'Program',
    price: 'Free',
    period: 'during early access',
    description: 'For large organizations with complex needs',
    features: [
      'Unlimited volunteers',
      'Multiple organizations',
      'All features',
      'API access',
      'Bulk import/export',
      'Custom integrations',
      'Custom training & onboarding',
    ],
    cta: 'Sign Up Free',
    ctaLink: 'https://app.volunteerclear.com/login',
    highlighted: false,
  },
];
</script>

<template>
  <section id="pricing" class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <div class="inline-block mb-4">
          <span class="bg-primary-100 text-primary-700 px-4 py-2 rounded-full text-sm font-semibold">
            🎉 Early Access - All Features Free
          </span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
          Join Our Early Access Program
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Get full access to all features completely free during our early access period. Help us build the best volunteer management platform.
        </p>
      </div>

      <!-- Pricing Cards -->
      <div class="grid md:grid-cols-3 gap-8 lg:gap-12">
        <div
          v-for="tier in pricingTiers"
          :key="tier.id"
          :class="[
            'relative rounded-2xl border-2 p-8 flex flex-col',
            tier.highlighted
              ? 'border-primary-600 shadow-xl scale-105 bg-primary-50'
              : 'border-gray-200 bg-white',
          ]"
        >
          <!-- Popular Badge -->
          <div
            v-if="tier.highlighted"
            class="absolute -top-4 left-1/2 transform -translate-x-1/2 z-10"
          >
            <span class="inline-block bg-blue-600 text-white px-6 py-2 rounded-full text-sm font-bold shadow-lg border-2 border-white">
              ⭐ Recommended
            </span>
          </div>

          <!-- Tier Header -->
          <div class="mb-6">
            <h3 class="text-2xl font-bold text-gray-900 mb-2">{{ tier.name }}</h3>
            <p class="text-gray-600 text-sm">{{ tier.description }}</p>
          </div>

          <!-- Price -->
          <div class="mb-6">
            <div class="flex items-baseline">
              <span class="text-5xl font-bold text-gray-900">{{ tier.price }}</span>
              <span class="ml-2 text-gray-600">{{ tier.period }}</span>
            </div>
          </div>

          <!-- Features List -->
          <ul class="space-y-4 mb-8 flex-grow" role="list">
            <li
              v-for="(feature, index) in tier.features"
              :key="index"
              class="flex items-start"
            >
              <CheckIcon class="h-5 w-5 text-primary-600 flex-shrink-0 mt-0.5" />
              <span class="ml-3 text-gray-700">{{ feature }}</span>
            </li>
          </ul>

          <!-- CTA Button -->
          <CTAButton
            :text="tier.cta"
            :variant="tier.highlighted ? 'primary' : 'outline'"
            size="lg"
            :href="tier.ctaLink"
            class="w-full"
          />
        </div>
      </div>

      <!-- Additional Info -->
      <div class="mt-12 text-center space-y-4">
        <p class="text-gray-900 font-semibold text-lg">
          All tiers are completely free during early access
        </p>
        <p class="text-gray-600 max-w-2xl mx-auto">
          No credit card required. No hidden fees. Join now and lock in special pricing when we launch. Early access members will receive exclusive benefits and grandfathered rates.
        </p>
      </div>
    </div>
  </section>
</template>
