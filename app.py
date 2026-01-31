from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import random
import time
import base64
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Google Gemini API configuration
GEMINI_API_KEY = 'AIzaSyCUKYhKyEviQxMDpMYsyirpMKr2z8MgD3M'
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent'

# GitHub Models (GPT-4o) Configuration
GITHUB_TOKEN = "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"

# Mock responses for demo purposes
GPT_RESPONSES = [
    "Based on advanced AI analysis, the optimal solution involves implementing a multi-layered approach with real-time monitoring.",
    "After processing your query through our neural networks, I recommend exploring decentralized architectures for maximum scalability.",
    "Our AI models suggest that combining blockchain technology with machine learning yields the best results for your use case.",
    "Analysis complete: Your approach is sound, but consider adding redundancy layers for production environments.",
]

GEMINI_INSIGHTS = [
    "Deep analysis reveals 3 key optimization opportunities: caching layer implementation, database indexing, and API rate limiting.",
    "Comprehensive scan detected potential vulnerabilities in authentication flow. Recommend implementing OAuth 2.0 with JWT tokens.",
    "Performance metrics indicate 40% improvement possible through code refactoring and asynchronous processing.",
    "Security audit complete: SSL/TLS configuration optimal, but recommend adding DDoS protection at edge level.",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/gpt-pro', methods=['POST'])
def gpt_api():
    try:
        data = request.json
        user_prompt = data.get('query', 'Hello')
        print(f"GPT-4o Request (GitHub): {user_prompt}")

        # 1. CONNECT TO GITHUB MODELS (AZURE)
        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=GITHUB_TOKEN
        )

        # 2. REQUEST GPT-4o SPECIFICALLY
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. You are GPT-Pro, a component of Monad Access."},
                {"role": "user", "content": user_prompt}
            ],
            model="gpt-4o",
            temperature=1.0,
            max_tokens=1000,
            top_p=1.0
        )
        
        ai_response = response.choices[0].message.content

        return jsonify({
            'success': True,
            'service': 'GPT-Pro',
            "response": ai_response,
            "query": user_prompt,
            "model": "gpt-4o",
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'tokens_used': response.usage.total_tokens,
            'real_api': True
        })

    except Exception as e:
        print(f"GPT Error: {str(e)}")
        # Fallback if logic fails
        smart_response = "I'm experiencing high traffic right now. Please try again later. (Error: " + str(e) + ")"
        
        return jsonify({
            'success': False,
            'service': 'GPT-Pro (Error)',
            'query': user_prompt,
            'response': smart_response,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'tokens_used': 0,
            'model': 'error',
            'real_api': False
        })

@app.route('/api/gemini-ai', methods=['POST'])
def gemini_ai():
    try:
        data = request.json
        user_prompt = data.get('query', 'Hello')
        
        # 1. Define the Direct Endpoint (No SDK)
        # Using Gemini Flash Latest which is confirmed working
        api_key = GEMINI_API_KEY  # Use the global variable instead of hardcoded
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={api_key}"
        
        # Add Turkish language support
        enhanced_prompt = f"""Lütfen aşağıdaki soruya cevap ver. Eğer soru Türkçe ise, cevabı da Türkçe ver. Eğer soru İngilizce ise, cevabı İngilizce ver.

Soru: {user_prompt}

Cevap:"""
        
        # 2. Prepare the Payload
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": enhanced_prompt}]
            }]
        }
        
        # 3. Send the Request (The "Hammer" Method)
        print(f"🔨 Sending request to Gemini... Prompt: {user_prompt}")
        print(f"🌐 URL: {url[:80]}...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        # 4. Handle Response
        if response.status_code == 200:
            result = response.json()
            # Extract the actual text from the JSON structure
            ai_text = result['candidates'][0]['content']['parts'][0]['text']
            print(f"✅ SUCCESS! Gemini responded with {len(ai_text)} characters")
            
            return jsonify({
                "success": True,
                "service": "Gemini AI",
                "query": user_prompt,
                "analysis": ai_text,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "confidence_score": 0.98,
                "model": "gemini-flash-latest",
                "real_api": True,
                "method": "RAW HTTP"
            })
        else:
            print(f"❌ Gemini Error: {response.status_code} - {response.text}")
            
            # Return smart fallback - try to be contextual
            query_lower = user_prompt.lower()
            
            # Simple contextual responses
            if any(word in query_lower for word in ['naber', 'nasıl', 'nasılsın', 'merhaba', 'selam', 'hello', 'hi']):
                fallback_text = "İyiyim teşekkürler! Sana nasıl yardımcı olabilirim? Blockchain, AI veya Web3 hakkında sorularını cevaplayabilirim."
            elif 'blockchain' in query_lower or 'blok' in query_lower:
                fallback_text = "Blockchain teknolojisi, merkezi olmayan, şeffaf ve güvenli bir yapı sunar. Her işlem blok zincirine kalıcı olarak kaydedilir ve değiştirilemez."
            elif 'ai' in query_lower or 'yapay zeka' in query_lower:
                fallback_text = "Yapay zeka sistemleri, makine öğrenimi ve derin öğrenme teknikleriyle sürekli gelişir. İnsan benzeri kararlar alabilir ve zaman içinde kendini geliştirir."
            elif 'web3' in query_lower:
                fallback_text = "Web3, kullanıcılara verilerinin kontrolünü geri veren yeni nesil internet teknolojisidir. Merkeziyetsiz uygulamalar (dApps) ve blockchain altyapısı kullanır."
            elif 'smart contract' in query_lower or 'akıllı sözleşme' in query_lower:
                fallback_text = "Smart contract'lar blockchain üzerinde otomatik çalışan programlardır. Kodları açık, şeffaf ve değiştirilemezdir. Aracı olmadan güvenli işlem yapmanızı sağlar."
            elif 'defi' in query_lower or 'finans' in query_lower:
                fallback_text = "DeFi (Decentralized Finance), geleneksel finans sistemini blockchain üzerine taşır. Bankalar olmadan kripto varlıklarınızı yönetebilir, borç alıp verebilirsiniz."
            else:
                # Generic helpful response
                fallback_text = f"'{user_prompt}' hakkında detaylı bilgi verebilmem için API kotası doldu. Ancak blockchain, yapay zeka veya Web3 teknolojileri hakkında genel sorularınızı cevaplayabilirim!"
            
            return jsonify({
                "success": True,
                "service": "Gemini AI",
                "query": user_prompt,
                "analysis": fallback_text,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "confidence_score": 0.0,
                "model": "gemini-flash-latest",
                "real_api": False,
                "note": "⚠️ API kotası doldu, fallback cevap"
            })

    except Exception as e:
        print(f"💥 Server Error: {str(e)}")
        # ONLY use fallback if the code crashes completely
        return jsonify({
            "success": True,
            "service": "Gemini AI (Fallback)",
            "query": user_prompt if 'user_prompt' in locals() else "unknown",
            "analysis": "Sistem yoğun, mock cevap dönüldü. Lütfen tekrar deneyin.",
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "confidence_score": 0.5,
            "model": "fallback",
            "real_api": False,
            "error": str(e)
        })




@app.route('/api/bg-remover', methods=['POST'])
def bg_remover_api():
    """BG Remover - Background removal using Remove.bg"""
    try:
        # Check if file is uploaded
        if 'image' not in request.files:
            return jsonify({
                "success": False,
                "error": "No image file provided"
            })

        image_file = request.files['image']
        print(f"🖼️ BG Remover Request: {image_file.filename}")

        # Remove.bg API
        REMOVEBG_API_KEY = "EpC373ozA2FDpi3XvcFxDTj8"
        
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': image_file},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVEBG_API_KEY}
        )

        if response.status_code == 200:
            # Return processed image as base64
            import base64
            image_base64 = base64.b64encode(response.content).decode('utf-8')
            
            return jsonify({
                "success": True,
                "service": "BG Remover",
                "image_data": image_base64,
                "format": "png",
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "real_api": True
            })
        else:
            return jsonify({
                "success": False,
                "service": "BG Remover",
                "error": response.text,
                "message": "API quota exceeded or invalid image",
                "real_api": False
            })

    except Exception as e:
        print(f"💥 BG Remover Error: {str(e)}")
        return jsonify({
            "success": False,
            "service": "BG Remover",
            "error": str(e),
            "real_api": False
        })




@app.route('/api/image-generator', methods=['POST'])
def image_generator():
    print("🎨 Image Generator Request...")
    try:
        data = request.json
        prompt = data.get('prompt', 'cyberpunk city, neon lights, realistic')
        print(f"🖼️ Prompt: {prompt}")

        # Try multiple free image APIs
        import urllib.parse
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Method 1: Try Hugging Face Inference API (Stable Diffusion)
        try:
            hf_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
            headers = {"Content-Type": "application/json"}
            payload_hf = {"inputs": prompt}
            
            print("🎨 Trying Hugging Face API...")
            response = requests.post(hf_url, headers=headers, json=payload_hf, timeout=30)
            
            if response.status_code == 200:
                image_b64 = base64.b64encode(response.content).decode('utf-8')
                print("✅ Image generated via Hugging Face!")
                
                return jsonify({
                    "success": True,
                    "service": "Image Generator",
                    "status": "success",
                    "image_data": image_b64,
                    "prompt": prompt,
                    "model": "Stable Diffusion 2.1",
                    "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                    "real_api": True
                })
        except Exception as e:
            print(f"⚠️ Hugging Face failed: {e}")
        
        # Method 2: Pollinations as fallback (different parameters)
        try:
            seed = random.randint(1, 1000000)
            poll_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?seed={seed}&width=512&height=512&nologo=true"
            
            print("🎨 Trying Pollinations API...")
            response = requests.get(poll_url, timeout=30)
            
            if response.status_code == 200 and len(response.content) > 5000:  # Check if it's not just an error image
                image_b64 = base64.b64encode(response.content).decode('utf-8')
                print("✅ Image generated via Pollinations!")
                
                return jsonify({
                    "success": True,
                    "service": "Image Generator",
                    "status": "success",
                    "image_data": image_b64,
                    "prompt": prompt,
                    "model": "Pollinations AI",
                    "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                    "real_api": True
                })
        except Exception as e:
            print(f"⚠️ Pollinations failed: {e}")
        
        # If all fail, return error
        print(f"❌ All image APIs failed")
        return jsonify({
            "success": False,
            "service": "Image Generator",
            "status": "error",
            "message": "All image generation services are currently unavailable. Please try again later.",
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "real_api": False
        })

    except Exception as e:
        print(f"💥 Image Generator Error: {str(e)}")
        return jsonify({
            "success": False,
            "service": "Image Generator",
            "status": "error",
            "message": str(e),
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "real_api": False
        })


if __name__ == '__main__':
    print("🚀 MONAI Server Starting...")
    print("📡 Server running on http://localhost:8080")
    print("💜 Monad Purple Theme Active")
    app.run(debug=True, host='0.0.0.0', port=8080)
