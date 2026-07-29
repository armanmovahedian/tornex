# بلاک‌ها

هر بلاک ACF داخل یک پوشه‌ی جدا به‌ازای نام خودش قرار می‌گیره:

```
blocks/
  {block-name}/
    block.json
    render.php
    style.css
    README.md
```

بلاک‌ها به‌صورت خودکار توسط `functions.php` (تابع `tornex_register_blocks`) اسکن و رجیستر می‌شن — نیازی به اضافه‌کردن دستی نیست.
