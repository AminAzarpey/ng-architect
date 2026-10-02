---
name: primeng
description: >-
  Builds and reviews Angular UIs with PrimeNG (primeng.org) v21 — 90+ components
  and directives. Trigger when adding/using p-* components (Table, Select,
  MultiSelect, AutoComplete, DatePicker, Dialog, Drawer, Toast, Menu/Menubar,
  Button, Tree, etc.), the pInputText/pTooltip/pRipple/pStyleClass directives,
  configuring providePrimeNG, theming with @primeuix/themes presets and design
  tokens, dark mode, passthrough (pt)/unstyled mode, Tailwind integration,
  PrimeIcons, or MessageService/ConfirmationService/DialogService.
license: MIT
metadata:
  author: Distilled from primeng.org (primefaces/primeng llms docs)
  version: "1.0"
  targets: PrimeNG v21
---

# PrimeNG Developer Guidelines

PrimeNG is a large, design-agnostic Angular UI library. This skill targets **v21**.

1. **Standalone-first.** Components are standalone (v17+) — import the component class or its
   `XxxModule` into the consuming component's `imports`; there is no root module to register.
   Always **check the project's installed `primeng` version** before generating code; the
   theming model changed substantially at v18.

2. **Set up the provider once.** `providePrimeNG({ theme: { preset } })` + `provideAnimationsAsync()`
   in `app.config.ts`, and import PrimeIcons CSS. See [installation](references/installation.md).

3. **Theme with design tokens, not CSS overrides.** Pick a preset (Aura/Material/Lara/Nora),
   customize via `definePreset`, and scope per-instance with the `dt` input. Reach for `pt`
   (pass through) only when the component API lacks an option, and CSS class overrides last.
   See [theming](references/theming.md) and [styling-integration](references/styling-integration.md).

4. **Service-backed components need providers + a host element.** Toast→`MessageService`+`<p-toast/>`,
   ConfirmDialog→`ConfirmationService`+`<p-confirmdialog/>`, DynamicDialog→`DialogService`.
   See [services](references/services.md).

5. **Content & data use templates.** Customize slots with `<ng-template #slot>` / `pTemplate`
   (e.g. Table columns, Select items). Two-way bind form components with `[(ngModel)]` or
   reactive `formControlName`. Each component reference lists its inputs/outputs/templates.

## Setup & cross-cutting guides

- **Installation & setup** — install, `providePrimeNG`, animations, first component. Read [installation.md](references/installation.md)
- **Configuration** — global options: ripple, inputVariant, zIndex, locale/translations, filter modes, CSP. Read [configuration.md](references/configuration.md)
- **Theming** — styled mode, presets, design tokens, `definePreset`, dark mode, scoped tokens, CSS layers. Read [theming.md](references/theming.md)
- **Styling integration** — Tailwind (`tailwindcss-primeui`), pass through (`pt`), unstyled mode, custom icons. Read [styling-integration.md](references/styling-integration.md)
- **Icons** — PrimeIcons usage and constants. Read [icons.md](references/icons.md)
- **RTL** — right-to-left support. Read [rtl.md](references/rtl.md)
- **Utility directives** — Ripple, StyleClass, Tooltip, FocusTrap, AutoFocus, KeyFilter, AnimateOnScroll, DragDrop. Read [directives.md](references/directives.md)
- **Services** — MessageService, ConfirmationService, DialogService. Read [services.md](references/services.md)
- **Accessibility** — WCAG/ARIA guidance. Read [accessibility.md](references/accessibility.md)

## Components

Each component has a focused reference (import, key inputs/outputs/templates, a minimal example,
and a link to the full API). Open the one you need:

### Form

- **AutoComplete** (`p-autocomplete`) — AutoComplete is an input component that provides real-time suggestions when being typed [autocomplete](references/components/autocomplete.md)
- **CascadeSelect** (`p-cascadeselect`) — CascadeSelect displays a nested structure of options [cascadeselect](references/components/cascadeselect.md)
- **Checkbox** (`p-checkbox`) — Checkbox is an extension to standard checkbox element with theming [checkbox](references/components/checkbox.md)
- **ColorPicker** (`p-colorpicker`) — ColorPicker is an input component to select a color [colorpicker](references/components/colorpicker.md)
- **DatePicker** (`p-datepicker`) — DatePicker is an input component to select a date [datepicker](references/components/datepicker.md)
- **Editor** (`p-editor`) — Editor is rich text editor component based on Quill [editor](references/components/editor.md)
- **Float Label** (`p-floatlabel`) — FloatLabel appears on top of the input field when focused [floatlabel](references/components/floatlabel.md)
- **Fluid** (`p-fluid`) — Fluid is a layout component to make descendant components span full width of their container [fluid](references/components/fluid.md)
- **IconField** (`p-iconfield`) — IconField wraps an input and an icon [iconfield](references/components/iconfield.md)
- **Ifta Label** (`p-iftalabel`) — IftaLabel is used to create infield top aligned labels [iftalabel](references/components/iftalabel.md)
- **InputGroup** (`p-inputgroup`) — Text, icon, buttons and other content can be grouped next to an input [inputgroup](references/components/inputgroup.md)
- **InputMask** — InputMask component is used to enter input in a certain format such as numeric, date, currency and phone [inputmask](references/components/inputmask.md)
- **InputNumber** (`p-inputnumber`) — InputNumber is an input component to provide numerical input [inputnumber](references/components/inputnumber.md)
- **Otp Input** (`p-inputotp`) — Input Otp is used to enter one time passwords [inputotp](references/components/inputotp.md)
- **InputText** (`pInputText`) — InputText is an extension to standard input element with theming and keyfiltering [inputtext](references/components/inputtext.md)
- **KeyFilter** (`pKeyFilter`) — KeyFilter is a directive to restrict individual key strokes. In order to restrict the whole input, use InputNumber or InputMask instead [keyfilter](references/components/keyfilter.md)
- **Knob** (`p-knob`) — Knob is a form component to define number inputs with a dial [knob](references/components/knob.md)
- **Listbox** (`p-listbox`) — Listbox is used to select one or more values from a list of items [listbox](references/components/listbox.md)
- **MultiSelect** (`p-multiselect`) — MultiSelect is used to select multiple items from a collection [multiselect](references/components/multiselect.md)
- **Password** (`p-password`) — Password displays strength indicator for password fields [password](references/components/password.md)
- **RadioButton** (`p-radiobutton`) — RadioButton is an extension to standard radio button element with theming [radiobutton](references/components/radiobutton.md)
- **Rating** (`p-rating`) — Rating component is a star based selection input [rating](references/components/rating.md)
- **Select** (`p-select`) — Select is used to choose an item from a collection of options [select](references/components/select.md)
- **SelectButton** (`p-selectbutton`) — SelectButton is used to choose single or multiple items from a list using buttons [selectbutton](references/components/selectbutton.md)
- **Slider** (`p-slider`) — Slider is a component to provide input with a drag handle [slider](references/components/slider.md)
- **Textarea** (`pTextarea`) — Textarea adds styling and autoResize functionality to standard textarea element [textarea](references/components/textarea.md)
- **ToggleButton** (`p-togglebutton`) — ToggleButton is used to select a boolean value using a button [togglebutton](references/components/togglebutton.md)
- **ToggleSwitch** (`p-toggleswitch`) — ToggleSwitch is used to select a boolean value [toggleswitch](references/components/toggleswitch.md)
- **TreeSelect** (`p-treeselect`) — TreeSelect is a form component to choose from hierarchical data [treeselect](references/components/treeselect.md)

### Button

- **Button** (`p-button` / `pButton` directive) — extension to the standard button with icons and theming; the `pButton` directive also styles native `<button>` and `<a routerLink>` elements [button](references/components/button.md)
- **Speed Dial** (`p-speeddial`) — SpeedDial is a floating button with a popup menu [speeddial](references/components/speeddial.md)
- **SplitButton** (`p-splitbutton`) — SplitButton groups a set of commands in an overlay with a default action item [splitbutton](references/components/splitbutton.md)

### Data

- **DataView** (`p-dataview`) — DataView displays data in grid grid-cols-12 gap-4 or list layout with pagination and sorting features [dataview](references/components/dataview.md)
- **OrderList** (`p-orderlist`) — OrderList is used to sort a collection [orderlist](references/components/orderlist.md)
- **Organization Chart** — OrganizationChart visualizes hierarchical organization data [organizationchart](references/components/organizationchart.md)
- **Paginator** (`p-paginator`) — Paginator displays data in paged format and provides navigation between pages [paginator](references/components/paginator.md)
- **PickList** (`p-picklist`) — PickList is used to reorder items between different lists [picklist](references/components/picklist.md)
- **Virtual Scroller** — VirtualScroller is a performance-approach to handle huge data efficiently [scroller](references/components/scroller.md)
- **Table** (`p-table`) — Table displays data in tabular format [table](references/components/table.md)
- **Timeline** (`p-timeline`) — Timeline visualizes a series of chained events [timeline](references/components/timeline.md)
- **Tree** (`p-tree`) — Tree is used to display hierarchical data [tree](references/components/tree.md)
- **TreeTable** (`p-treetable`) — TreeTable is used to display hierarchical data in tabular format [treetable](references/components/treetable.md)

### Panel

- **Accordion** (`p-accordion`) — Accordion groups a collection of contents in tabs [accordion](references/components/accordion.md)
- **Card** (`p-card`) — Card is a flexible container component [card](references/components/card.md)
- **Divider** (`p-divider`) — Divider is used to separate contents [divider](references/components/divider.md)
- **Fieldset** (`p-fieldset`) — Fieldset is a grouping component with a content toggle feature [fieldset](references/components/fieldset.md)
- **Panel** (`p-panel`) — Panel is a container component with an optional content toggle feature [panel](references/components/panel.md)
- **Scroll Panel** (`p-scrollpanel`) — ScrollPanel is a cross browser, lightweight and skinnable alternative to native browser scrollbar [scrollpanel](references/components/scrollpanel.md)
- **Splitter** (`p-splitter`) — Splitter is utilized to separate and resize panels [splitter](references/components/splitter.md)
- **Stepper** (`p-stepper`) — The Stepper component displays a wizard-like workflow by guiding users through the multi-step progression [stepper](references/components/stepper.md)
- **Tabs** (`p-tabs`) — Tabs is a container component to group content with tabs [tabs](references/components/tabs.md)
- **Toolbar** (`p-toolbar`) — Toolbar is a grouping component for buttons and other content [toolbar](references/components/toolbar.md)

### Overlay

- **ConfirmDialog** (`p-confirmdialog`) — ConfirmDialog is backed by a service utilizing Observables to display confirmation windows easily that can be shared by multiple actions on the same component [confirmdialog](references/components/confirmdialog.md)
- **ConfirmPopup** (`p-confirmpopup`) — ConfirmPopup displays a confirmation overlay displayed relatively to its target [confirmpopup](references/components/confirmpopup.md)
- **Dialog** (`p-dialog`) — Dialog is a container to display content in an overlay window [dialog](references/components/dialog.md)
- **Drawer** (`p-drawer`) — Drawer is a container component displayed as an overlay [drawer](references/components/drawer.md)
- **Dynamic Dialog** — Dialogs can be created dynamically with any component as the content using a DialogService [dynamicdialog](references/components/dynamicdialog.md)
- **Overlay API - PrimeNG** (`p-overlay`) — This API allows overlay components to be controlled from the PrimeNG. In this way, all overlay components in the application can have the same behavior [overlay](references/components/overlay.md)
- **Popover** (`p-popover`) — Popover is a container component that can overlay other components on page [popover](references/components/popover.md)
- **Tooltip** (`pTooltip`) — Tooltip directive provides advisory information for a component. Tooltip is integrated within various PrimeNG components [tooltip](references/components/tooltip.md)

### File

- **FileUpload** (`p-fileupload`) — FileUpload is an advanced uploader with dragdrop support, multi file uploads, auto uploading, progress tracking and validations [fileupload](references/components/fileupload.md)

### Menu

- **Breadcrumb** (`p-breadcrumb`) — Breadcrumb provides contextual information about page hierarchy [breadcrumb](references/components/breadcrumb.md)
- **ContextMenu** (`p-contextmenu`) — ContextMenu displays an overlay menu on right click of its target [contextmenu](references/components/contextmenu.md)
- **Dock** (`p-dock`) — Dock is a navigation component consisting of menuitems [dock](references/components/dock.md)
- **MegaMenu** (`p-megamenu`) — MegaMenu is navigation component that displays submenus together [megamenu](references/components/megamenu.md)
- **Menu** (`p-menu`) — Menu is a navigation / command component that supports dynamic and static positioning [menu](references/components/menu.md)
- **Menubar** (`p-menubar`) — Menubar is a horizontal menu component [menubar](references/components/menubar.md)
- **PanelMenu** (`p-panelmenu`) — PanelMenu is a hybrid of Accordion and Tree components [panelmenu](references/components/panelmenu.md)
- **Steps** (`p-steps`) — [steps](references/components/steps.md)
- **TieredMenu** (`p-tieredmenu`) — TieredMenu displays submenus in nested overlays [tieredmenu](references/components/tieredmenu.md)

### Messages

- **Message** (`p-message`) — Message component is used to display inline messages [message](references/components/message.md)
- **Toast** (`p-toast`) — Toast is used to display messages in an overlay [toast](references/components/toast.md)

### Media

- **Carousel** (`p-carousel`) — Carousel is a content slider featuring various customization options [carousel](references/components/carousel.md)
- **Gallery** (`p-galleria`) — Galleria is an advanced content gallery component [galleria](references/components/galleria.md)
- **Image** (`p-image`) — Displays an image with preview and tranformation options [image](references/components/image.md)
- **ImageCompare** (`p-imagecompare`) — Compare two images side by side with a slider [imagecompare](references/components/imagecompare.md)

### Chart

- **Chart** (`p-chart`) — Chart components are based on Charts.js 3.3.2+, an open source HTML5 based charting library [chart](references/components/chart.md)

### Misc

- **Animate On Scroll** (`pAnimateOnScroll`) — AnimateOnScroll is used to apply animations to elements when entering or leaving the viewport during scrolling [animateonscroll](references/components/animateonscroll.md)
- **AutoFocus** (`pAutoFocus`) — AutoFocus manages focus on focusable element on load [autofocus](references/components/autofocus.md)
- **Avatar** (`p-avatar`) — Avatar represents people using icons, labels and images [avatar](references/components/avatar.md)
- **Badge** (`p-badge`) — Badge is a small status indicator for another element [badge](references/components/badge.md)
- **BlockUI** (`p-blockui`) — BlockUI can either block other components or the whole page [blockui](references/components/blockui.md)
- **Chip** (`p-chip`) — Chip represents entities using icons, labels and images [chip](references/components/chip.md)
- **Drag and Drop** (`pDraggable / pDroppable`) — pDraggable and pDroppable directives apply drag-drop behaviors to any element [dragdrop](references/components/dragdrop.md)
- **Focus Trap** (`pFocusTrap`) — Focus Trap keeps focus within a certain DOM element while tabbing [focustrap](references/components/focustrap.md)
- **Inplace** (`p-inplace`) — Inplace provides an easy to do editing and display at the same time where clicking the output displays the actual content [inplace](references/components/inplace.md)
- **MeterGroup** (`p-metergroup`) — MeterGroup displays scalar measurements within a known range [metergroup](references/components/metergroup.md)
- **ProgressBar** (`p-progressbar`) — ProgressBar is a process status indicator [progressbar](references/components/progressbar.md)
- **ProgressSpinner** — ProgressSpinner is a process status indicator [progressspinner](references/components/progressspinner.md)
- **Ripple** (`pRipple`) — Ripple directive adds ripple effect to the host element [ripple](references/components/ripple.md)
- **Scroll Top** (`p-scrolltop`) — ScrollTop gets displayed after a certain scroll position and used to navigates to the top of the page quickly [scrolltop](references/components/scrolltop.md)
- **Skeleton** (`p-skeleton`) — Skeleton is a placeholder to display instead of the actual content [skeleton](references/components/skeleton.md)
- **StyleClass** (`pStyleClass`) — StyleClass manages css classes declaratively to during enter/leave animations or just to toggle classes on an element [styleclass](references/components/styleclass.md)
- **Tag** (`p-tag`) — Tag component is used to categorize content [tag](references/components/tag.md)
- **Terminal** (`p-terminal`) — [terminal](references/components/terminal.md)

---

For exhaustive API, theming tokens, and more examples on any component, see `https://primeng.org/<component>`.
