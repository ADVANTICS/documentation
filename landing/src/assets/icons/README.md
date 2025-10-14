I am using [ astro-icons ](https://www.astroicon.dev/) to comfortably manage icons. They are also optimized on the fly.

This plugins looks for `.svg` files in the `src/icons` folder. Then you can use them:

```js
---
import {Icon} from "astro-icon/component"
---
<Icon name="advantics">
```

See how to install Icon sets in [the customization section](https://www.astroicon.dev/guides/customization/).
