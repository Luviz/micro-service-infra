import fetch from "node-fetch";

const blogUrl = `http://localhost:8010`;
// Resolvers define the technique for fetching the types defined in the
// schema. This resolver retrieves books from the "books" array above.
export const resolvers = {
  Query: {
    blogs: async () => {
      const res = await fetch(`${blogUrl}/blog`)
        .then((r) => r.json())
        .then((d) => d.Items);
      return res;
    },
    getBlog: async (p, { id }) => {
      const res = await fetch(`${blogUrl}/blog/${id}`)
        .then((r) => r.json())
        .then((d) => d.Item);
      return res;
    },
  },
};
