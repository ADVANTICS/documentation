import { reference, z, defineCollection } from "astro:content";

const applicationsAndVacanciesBase = z.object({
  img: z.string(),
  alt: z.string(),
  title: z.string(),
  href: z.string().optional(),
  cardImgClasses: z.string().optional(),
  keypoints: z.array(z.string()),
});

const careers = defineCollection({
  type: "content",
  schema: applicationsAndVacanciesBase.extend({
    offer: z.array(z.string()),
    tasks: z.array(z.string()),
    description: z.string(),
    code: z.string(),
    extraDescription: z.string().optional(),
  }),
});

const applications = defineCollection({
  type: "content",
  schema: applicationsAndVacanciesBase.extend({
    description: z.string(),
    canonicalIndustry: reference("industries").optional(),
    showDiagramOn: reference("industries").optional(),
    heroImgClasses: z.string().optional(),
    products: z.union([
      z.array(reference("products")),
      z.array(
        z.object({
          industry: reference("industries"),
          products: z.array(reference("products")),
        }),
      ),
    ]),
    diagram: z.string().optional(),
  }),
});

// 4. Each collection entry will have an unique id equal to the filename
// There is no need to add an id field in the schema
const industries = defineCollection({
  type: "content",
  schema: z.object({
    order: z.number(),
    products: z.array(reference("products")),
    href: z.string().optional(),
    cardImgClasses: z.string().optional(),
    heroImg: z.string().optional(),
    img: z.string(),
    heroImgClasses: z.string().optional(),
    alt: z.string(),
    title: z.string(),
    applications: z.array(reference("applications")),
    description: z.string(),
  }),
});
// 5. Data collection, opposite to content collections, does not have a render
// method that will return an Astro component that we can use to show
// the rendered markdown to html
const products = defineCollection({
  type: "data",
  schema: z.object({
    docsReady: z.boolean().optional(),
    keywords: z.string().optional(),
    isComingSoon: z.boolean().optional(),
    sortNumber: z.number().optional(),
    storeHref: z.string().optional(),
    characteristics: z.array(z.string()).optional(),
    applications: z.array(z.string()).optional(),
    docsHref: z.string().optional(),
    codename: z.string(),
    variantClarification: z.record(z.string()).optional(),
    OGimg: z.string().optional(),
    card: z.object({
      name: z.string(),
      imgScale: z.string().optional(),
      imgRotation: z.string().optional(),
      img: z.string(),
      alt: z.string(),
      description: z.string(),
      keyPoints: z.record(z.record(z.string())).optional(),
    }),
    header: z.object({
      imgClasses: z.string().optional(),
      name: z.string(),
      title: z.string(),
      img: z.string(),
      alt: z.string(),
      description: z.string(),
    }),
    hardwareDescription: z.array(z.string()),
    techData: z.record(
      z.array(z.object({ name: z.string(), value: z.string().nullable() })),
    ),

    carousel: z.array(
      z.object({
        path: z.string(),
        alt: z.string(),
        caption: z.string().optional(),
      }),
    ),
    attachments: z
      .array(
        z.object({
          variant: z.array(z.string()),
          name: z.string(),
          href: z.string(),
        }),
      )
      .optional(),
  }),
});

const blog = defineCollection({
  type: "content",
  schema: z
    .object({
      title: z.string(),
      date: z.date(),
      strap: z.string().optional(),
      isGoodForRelease: z.boolean(),
      author: z.string(),
      description: z.string(),
      img: z.string(),
      slideImg: z.string().optional(),
      OGimg: z.string().optional(),
      alt: z.string(),
      slideOnly: z.boolean().optional(),
      href: z.string().optional(),
    })
    .refine(
      (data) => {
        if (data.slideOnly !== undefined) {
          return typeof data.href === "string" && data.href.length > 0;
        }
        return true;
      },
      {
        message: "href is required when slideOnly is defined",
        path: ["href"],
      },
    ),
});
// 6. Export a single `collections` object to register your collection(s)
//    This key should match your collection directory name in "src/content"
//    Re-assign property names if needed:
export const collections = {
  careers,
  applications,
  products,
  industries,
  blog,
};
