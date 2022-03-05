const books = [
  {
    title: "The Awakening",
    author: "Kate Chopin",
  },
  {
    title: "City of Glass",
    author: "Paul Auster",
  },
];

// Resolvers define the technique for fetching the types defined in the
// schema. This resolver retrieves books from the "books" array above.
export const resolvers = {
  Query: {
    books: () => {
      console.log("hello", books);
      return books;
    },
    meh: (parent, { req }) => {
      const { meh } = req;
      console.log(meh, req);
      const res = [];
      for (const book of books) {
        books.title = `${meh} ${book.title}`;
        res.push({
          title: `${meh} ${book.title}`,
          author: book.title,
        });
      }
      return res;
    },
  },
};
