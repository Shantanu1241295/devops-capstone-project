from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for API routes
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Configure Talisman for security headers (HSTS, X-Frame-Options, CSP, etc.)
    # Note: Set force_https=True when deploying to a production HTTPS environment
    csp = {
        'default-src': '\'self\'',
        'script-src': ['\'self\'', '\'unsafe-inline\''],
        'style-src': ['\'self\'', '\'unsafe-inline\'']
    }
    
    Talisman(
        app, 
        content_security_policy=csp, 
        force_https=False, 
        strict_transport_security=True,
        session_cookie_secure=False # Set to True in production with HTTPS
    )
    
    @app.route("/")
    def health_check():
        return {"status": "SECURE", "message": "Security headers and CORS configured successfully."}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)
