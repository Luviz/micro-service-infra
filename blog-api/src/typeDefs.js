import { gql } from "apollo-server";

export default gql`
  type Book {
    title: String
    author: String
  }

  input BookReq {
    meh: String
  }

  type Query {
    books: [Book]
    meh(req: BookReq): [Book]
  }
`;
