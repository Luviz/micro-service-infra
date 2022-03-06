const path = require("path");
const common = require("./webpack.common");
const cleanWebpackPlugin = require("clean-webpack-plugin");

module.exports = {
  output: {
    filename: "server.js",
    path: path.resolve(__dirname, "dist"),
  },
  resolve: {
    extensions: [".js"],
  },
  target: "node",
  watch: true,
};

const merge = require("webpack-merge");
const nodeExternals = require("webpack-node-externals");

module.exports = merge.merge(common, {
  devtool: "source-map",
  entry: [path.join(__dirname, "src/index.js")],
  externals: [nodeExternals({})],
  mode: "production",
  plugins: [new cleanWebpackPlugin.CleanWebpackPlugin()],
});
