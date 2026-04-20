import ja from '~/i18n/ja.json';
import en from '~/i18n/en.json';

export type Locale = 'ja' | 'en';
export const locales: Locale[] = ['ja', 'en'];
export const defaultLocale: Locale = 'ja';

const dict = { ja, en } as const;

export type Dict = typeof ja;

export function t(locale: Locale): Dict {
  return dict[locale] as Dict;
}

export function isLocale(value: string | undefined): value is Locale {
  return value === 'ja' || value === 'en';
}

/** Detect locale from a URL pathname like /ja/menu or /en/ */
export function localeFromPath(pathname: string): Locale {
  const segment = pathname.split('/').filter(Boolean)[0];
  return isLocale(segment) ? segment : defaultLocale;
}

/** Swap the locale segment in a pathname. /ja/menu -> /en/menu */
export function swapLocale(pathname: string, to: Locale): string {
  const parts = pathname.split('/').filter(Boolean);
  if (parts.length === 0 || !isLocale(parts[0])) return `/${to}/`;
  parts[0] = to;
  const trailing = pathname.endsWith('/') ? '/' : '';
  return `/${parts.join('/')}${trailing}`;
}

export const SOCIAL = {
  instagramHandle: 'bkc_yu____me',
  instagramUrl: 'https://www.instagram.com/bkc_yu____me/',
  instagramDm: 'https://ig.me/m/bkc_yu____me',
  threadsUrl: 'https://www.threads.net/@bkc_yu____me',
  email: 'contact@example.com',
} as const;
