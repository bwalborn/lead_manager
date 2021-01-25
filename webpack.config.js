module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/ ,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}

// Just loads the babel loader -> key for react