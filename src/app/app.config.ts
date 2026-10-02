import {
  ApplicationConfig,
  provideBrowserGlobalErrorListeners,
  provideZonelessChangeDetection,
} from '@angular/core';
import { provideRouter } from '@angular/router';
import Aura from '@primeuix/themes/aura';
import { providePrimeNG } from 'primeng/config';

import { routes } from './app.routes';

declare const PRIMEUI_LICENSE_KEY: string;

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZonelessChangeDetection(),
    provideRouter(routes),
    providePrimeNG({
      theme: { preset: Aura },
      license:
        typeof PRIMEUI_LICENSE_KEY === 'undefined'
          ? undefined
          : PRIMEUI_LICENSE_KEY,
    }),
  ],
};
