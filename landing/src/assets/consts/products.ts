export const releaseStates = {
  availableForOrder: "availableForOrder",
  comingSoon: "comingSoon",
  newRelease: "newRelease",
} as const;

export const releaseStatusMap = {
  [releaseStates.availableForOrder]: {
    ribbon: "Available for order",
    header: "Available for order",
  },
  [releaseStates.newRelease]: {
    ribbon: "New Release",
    header: "New Release",
  },
  [releaseStates.comingSoon]: { ribbon: "Coming soon", header: "Coming soon" },
} as const;

export const contactText = ({
  subject,
  name,
}: {
  name: string;
  subject: "INFO" | "ORDER";
}) => {
  switch (subject) {
    case "INFO":
      return { text: `Hello, I would like to inquire about the ${name}` };

    case "ORDER":
      return { text: `Hello, I would be interested in ordering ${name}` };
  }
  throw new Error("Subject not found");
};
