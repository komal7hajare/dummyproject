from flask import Flask, jsonify, request, abort
import trends

# creating a flask app
app = Flask(__name__)
port = 3001

@app.route('/')
def greeting():
        return trends.api_response(200, 'Molins API Application up and running!')

    @app.route('/healthCheck', methods=['GET'])
    def healthCheck():
            return trends.api_response(200, 'App up and running!')

        @app.route('/api/direct', methods=["POST"])
        def direct_call():
                return trends.api_response(200, "Dummy Api direct executed!")

            @app.route('/api/trend', methods=["POST"])
            def trend_api():
                    return trends.api_response(200, 'Dummy Api trend executed!')

                @app.route("/api/filter", methods=["POST"])
                def postFilterLimit():    
                        return trends.api_response(200, 'Dummy Api filter executed!')

                    if __name__ == '__main__':
                            app.run(host='0.0.0.0',port=port)
