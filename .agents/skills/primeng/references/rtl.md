# RTL (Right-to-Left)

PrimeNG components support RTL natively via modern CSS (FlexBox + logical properties like `*-inline-start`). **No JavaScript configuration is needed** — just set the document text direction.

```html
<html dir="rtl"></html>
```

or scope it to a subtree:

```html
<div dir="rtl">
  <!-- PrimeNG components here render RTL -->
</div>
```

You can also set it via the `direction` CSS property.

**Limitation:** RTL is supported across the suite **except `Galleria` and `Carousel`** (planned for a future release). Verify against the installed version.
