# PrimeUI Community activation

This project chooses the PrimeUI Community License for eligible developers. PrimeNG 22 still requires an issued license key to remove the `Invalid PrimeUI License` notice. Open-source status does not activate a license automatically.

## Obtain your key

Register at the [PrimeUI Store](https://primeui.store), select the free Community license, confirm eligibility, and obtain your key. The [Community terms](https://primeui.dev/licenses/community) describe eligibility and annual renewal. Each developer working with PrimeUI needs the appropriate license; do not share a key in this repository.

## Local development

Create `.env.local` in the repository root, using `.env.example` as a template:

```dotenv
PRIMEUI_LICENSE_KEY=your-issued-community-license-key
```

Then restart the development server:

```sh
mise run dev
```

`.env.local` is ignored by Git and Prettier. The development/build launcher reads it, passes the value through Angular's `define` option, and the application supplies it to `providePrimeNG({ license: ... })`. Do not commit your issued key. If the variable is missing, the normal PrimeUI notice remains; the application does not hide or bypass license verification.

## Builds and CI

Use `mise run build` or `mise exec -- npm run build`. The same launcher reads `PRIMEUI_LICENSE_KEY` from the process environment, so a CI variable can supply it without a local file. An existing process environment value takes precedence over `.env.local`. The watch script uses the launcher too. Direct `ng` commands bypass it; use the project scripts when supplying a license.

The key is included in the browser bundle, as required for offline verification. PrimeUI says the key contains no sensitive data, but must not be published for others to reuse. CI does not need its own developer seat. Unit tests use the normal unlicensed configuration and do not establish license validity.

## Verify activation

Reload the running application and check that the license notice and license console warning are gone. Repeat against the production build served locally. A successful build alone does not prove a key is valid. If the notice remains, check that the key was issued for your license and is current, then restart or rebuild after correcting it.

Angular Material and Tailwind CSS remain installed and configured alongside PrimeNG. See [UI library choices](UI-LIBRARIES.md).

References: [PrimeNG installation](https://primeng.dev/installation), [PrimeUI Community License](https://primeui.dev/licenses/community).
