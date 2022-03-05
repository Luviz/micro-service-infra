import { ApolloServer } from "apollo-server";
import { resolvers } from "./resolvers";
import typeDefs from "./typeDefs";

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});

if (module.hot) {
  module.hot.accept();
  module.hot.dispose(() => {
    console.log("Module disposed");
  });
}
