---
name: add-route
description: Scaffold a new Flask route specifically for the Investing repo's web app, following its established patterns (blueprints in web/routes, Firebase auth, Firestore dual-mode, matching templates). Use when working in this Investing codebase and the user wants to add a route, endpoint, API, or page for this project.
---

# Add Route Skill

Scaffold a new Flask route following the project's established patterns.

## Triggers

- User asks to "add a route", "create an endpoint", "add an API", "create a new page"
- `/add-route <name>` command

## Workflow

### 1. Gather Requirements

Ask the user (if not provided):
- **Route name**: The blueprint name (e.g., `alerts`, `crypto`, `reports`)
- **URL prefix**: Where it will be mounted (e.g., `/alerts`, `/api/crypto`)
- **Has page?**: Does this need an HTML template or is it API-only?
- **Auth required?**: Should routes require Firebase authentication?

### 2. Create Route File

Create `web/routes/<name>.py` following this pattern:

```python
"""<Name> routes."""
from flask import Blueprint, jsonify, render_template, request, g

from src.firebase_config import require_auth
from src.data.firestore_service import firestore_service as fs, use_firestore

bp = Blueprint('<name>', __name__)


@bp.route('/')
@require_auth
def index():
    """<Name> page."""
    return render_template('<name>.html')


@bp.route('/api/list')
@require_auth
def api_list():
    """Get <name> data."""
    try:
        if use_firestore():
            data = fs.get_<name>(g.user_id)
        else:
            data = []
        return jsonify({'data': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/api/add', methods=['POST'])
@require_auth
def api_add():
    """Add new <name> item."""
    try:
        data = request.json
        if not data.get('required_field'):
            return jsonify({'error': 'required_field is required'}), 400

        if use_firestore():
            item_id = fs.add_<name>(g.user_id, data)
        else:
            item_id = None
        return jsonify({'success': True, 'id': item_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/api/delete/<item_id>', methods=['DELETE'])
@require_auth
def api_delete(item_id):
    """Delete <name> item."""
    try:
        if use_firestore():
            success = fs.delete_<name>(g.user_id, item_id)
        else:
            success = False
        return jsonify({'success': success})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

### 3. Create Template (if needed)

Create `web/templates/<name>.html` using existing patterns with Tailwind CSS and `fetchAPI()`.

### 4. Register Blueprint

Add to `web/app.py`:

```python
from web.routes import <name>
app.register_blueprint(<name>.bp, url_prefix='/<name>')
```

### 5. Add Firestore Methods (if using Firestore)

Add CRUD methods to `src/data/firestore_service.py`.

### 6. Update Firestore Rules

Add user-isolation rules to `firestore.rules`.

### 7. Verify

Run `python verify.py --quick` to ensure no import or lint errors.

## Key Patterns to Follow

- Always use `@require_auth` decorator for user-specific data
- Use `g.user_id` to get the authenticated user's ID
- Use `use_firestore()` check for dual-mode storage support
- Return JSON with `{'error': str(e)}` for error responses
- Use Tailwind CSS classes in templates
- Use `fetchAPI()` from `app.js` for frontend API calls
