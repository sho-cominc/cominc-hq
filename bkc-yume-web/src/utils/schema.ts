import type { Locale } from './i18n';
import { SOCIAL } from './i18n';
import nextEvent from '~/data/next-event.json';
import menu from '~/data/menu.json';

const SITE_URL = 'https://bkc-yume-web.pages.dev';
const BUSINESS_NAME = 'BLACK KITCHEN CAR ゆめ';
const BUSINESS_NAME_EN = 'BLACK KITCHEN CAR YUME';

export function organizationSchema(locale: Locale) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: locale === 'ja' ? BUSINESS_NAME : BUSINESS_NAME_EN,
    url: SITE_URL,
    logo: `${SITE_URL}/og.svg`,
    sameAs: [SOCIAL.instagramUrl, SOCIAL.threadsUrl],
    contactPoint: {
      '@type': 'ContactPoint',
      contactType: 'customer service',
      email: SOCIAL.email,
      url: SOCIAL.instagramDm,
      availableLanguage: ['Japanese', 'English'],
    },
  };
}

/**
 * FoodEstablishment fits a parfait kitchen car better than generic LocalBusiness.
 * No fixed address — areaServed encodes the mobile service area.
 */
export function foodEstablishmentSchema(locale: Locale) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FoodEstablishment',
    name: locale === 'ja' ? BUSINESS_NAME : BUSINESS_NAME_EN,
    image: `${SITE_URL}/og.svg`,
    url: SITE_URL,
    servesCuisine: locale === 'ja' ? 'パフェ' : 'Parfait',
    priceRange: '¥800-¥1000',
    paymentAccepted: locale === 'ja' ? '現金、各種キャッシュレス' : 'Cash, cashless',
    areaServed: [
      { '@type': 'City', name: locale === 'ja' ? '上越市' : 'Joetsu' },
      { '@type': 'City', name: locale === 'ja' ? '妙高市' : 'Myoko' },
    ],
    sameAs: [SOCIAL.instagramUrl, SOCIAL.threadsUrl],
    hasMenu: `${SITE_URL}/${locale}/menu`,
  };
}

export function menuSchema(locale: Locale) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Menu',
    name: locale === 'ja' ? 'メニュー' : 'Menu',
    inLanguage: locale === 'ja' ? 'ja-JP' : 'en-US',
    hasMenuSection: [
      {
        '@type': 'MenuSection',
        name: locale === 'ja' ? 'パフェ' : 'Parfait',
        hasMenuItem: menu.map((item) => ({
          '@type': 'MenuItem',
          name: locale === 'ja' ? item.name_ja : item.name_en,
          description: locale === 'ja' ? item.description_ja : item.description_en,
          offers: {
            '@type': 'Offer',
            price: String(item.price),
            priceCurrency: 'JPY',
          },
          suitableForDiet: [],
          ...(item.seasonal && {
            availability: 'https://schema.org/LimitedAvailability',
          }),
        })),
      },
    ],
  };
}

export function nextEventSchema(locale: Locale) {
  if (!nextEvent?.date) return null;
  const venue = locale === 'ja' ? nextEvent.venue_ja : nextEvent.venue_en;
  const address = locale === 'ja' ? nextEvent.address_ja : nextEvent.address_en;
  return {
    '@context': 'https://schema.org',
    '@type': 'FoodEvent',
    name: `${BUSINESS_NAME} @ ${venue}`,
    startDate: `${nextEvent.date}T${nextEvent.startTime}:00+09:00`,
    endDate: `${nextEvent.date}T${nextEvent.endTime}:00+09:00`,
    eventStatus: 'https://schema.org/EventScheduled',
    eventAttendanceMode: 'https://schema.org/OfflineEventAttendanceMode',
    location: {
      '@type': 'Place',
      name: venue,
      address: { '@type': 'PostalAddress', addressLocality: address },
    },
    organizer: {
      '@type': 'Organization',
      name: locale === 'ja' ? BUSINESS_NAME : BUSINESS_NAME_EN,
      url: SITE_URL,
    },
    image: `${SITE_URL}/og.svg`,
    url: `${SITE_URL}/${locale}/schedule`,
  };
}

export interface FaqItem {
  q_ja: string;
  q_en: string;
  a_ja: string;
  a_en: string;
}

export function faqPageSchema(locale: Locale, items: FaqItem[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map((item) => ({
      '@type': 'Question',
      name: locale === 'ja' ? item.q_ja : item.q_en,
      acceptedAnswer: {
        '@type': 'Answer',
        text: locale === 'ja' ? item.a_ja : item.a_en,
      },
    })),
  };
}
