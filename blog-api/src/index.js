import { ApolloServer } from "apollo-server";
import { resolvers } from "./resolvers.js";
import typeDefs from "./schema.gql";

const server = new ApolloServer({ typeDefs, resolvers });

const port = process.env["PORT"] || 8080;

server.listen({ port }).then(({ url }) => {
  console.log(`Server ready at ${url}`);
});

if (module.hot) {
  module.hot.accept();
  module.hot.dispose(() => {
    console.log("Module disposed");
  });
}
