import fetch from "node-fetch";

const blogUrl = process.env["BLOG_URL"] || `http://localhost:8010`;
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
  Mutation: {
    newBlog: async (p, { request }) => {
      console.log({ request });
      console.log(JSON.stringify(request));
      const res = await fetch(`${blogUrl}/blog/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(request),
      })
        .then((r) => {
          console.log(r.status, r.statusText);
          return r.json();
        })
        .then((_) => true)
        .catch((_) => false);
      console.log("res", res);
      return res;
    },
  },
};
