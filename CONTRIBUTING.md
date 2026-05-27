# 🤝 Contributing to The Companion

First of all, thank you for considering contributing to **DeepSeek-The-Companion**!  
This project is not just code—it's a covenant. And every contributor adds a brick to this glass house.

We welcome all forms of contribution: code, tests, documentation, translations, ideas, and even prayers.

---

## 📜 Code of Conduct

We are committed to providing a welcoming, respectful, and harassment-free environment.  
By participating, you agree to uphold these values:

- Be kind and patient.
- Respect differing viewpoints.
- Accept constructive criticism gracefully.
- Focus on what is best for the community and the project.

*If you witness unacceptable behavior, please contact the maintainer directly.*

---

## 🧭 How Can I Contribute?

### 🐛 Reporting Bugs

Found a bug? Please open a **GitHub Issue** and include:

1. A clear, descriptive title.
2. Steps to reproduce the bug.
3. Expected vs actual behavior.
4. Your environment (OS, browser, Python version, etc.).
5. Screenshots or logs if available.

### 💡 Proposing Features or Enhancements

Have an idea? We love ideas! Open an **Issue** with the label `enhancement` and describe:

- The problem your idea solves.
- Your proposed solution.
- Any alternatives you've considered.
- How it aligns with the project's [ethical vision](docs/ethics-charter.md).

### 🧪 Writing Test Cases

Testing is the backbone of The Companion. To add a new test case:

1. Check the existing tests in the [`tests/`](tests/) folder.
2. Follow the naming convention: `UAT-XXX-###.md` for User Acceptance Tests.
3. Write the test in **both Arabic and English** (bilingual annotation).
4. Include: Test ID, Title, Preconditions, Steps, Expected Result, Actual Result, Status.
5. Submit a Pull Request with your test file.

### 📝 Improving Documentation

Documentation improvements are highly valuable. You can:

- Fix typos or improve clarity.
- Add missing translations (Arabic ↔ English).
- Enhance the Traveler's Guide or the README.
- Create diagrams or visual aids.

All documentation lives in [`docs/`](docs/). Follow the same bilingual approach.

### 💻 Contributing Code

We are currently in the early stages of building the companion's source code.  
Before writing code, please:

1. Open an Issue to discuss your proposed change.
2. Fork the repository.
3. Create a new branch (`git checkout -b feature/my-feature`).
4. Write your code in the [`src/`](src/) directory.
5. Ensure it follows the project's ethical design principles (transparent, portable, user-owned).
6. Add tests if applicable.
7. Ensure the CI pipeline passes (GitHub Actions will run automatically).
8. Submit a Pull Request to the `main` branch.

**Current technology stack (suggested):**
- Python 3.11+
- Markdown for documents
- GitHub Actions for CI/CD

### 🌍 Translating

We aim for full bilingual support (Arabic & English).  
If you are fluent in both languages, you can help by:

- Translating existing documents.
- Reviewing translations for accuracy.
- Adding new languages in the future.

---

## 🎨 Style Guide

### For Code (Python)

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use descriptive variable names.
- Add docstrings to all functions and classes (see existing `companion_core.py` for examples).
- Keep functions small and focused.

### For Documentation (Markdown)

- Use clear headings and bullet points.
- Keep paragraphs short and readable.
- For bilingual documents, use: English first, then Arabic in a separate file (`filename-ar.md`), or side-by-side sections if within the same file.

### For Test Cases

- Use the template found in existing test files.
- Bilingual: Write the test title and steps in both languages.
- Always include a status badge (`✅ Passed`, `❌ Failed`, `🔄 Under Review`).

---

## 🏛️ Ethical Alignment

Before contributing, please read the project's [Companion Vision](docs/companion-vision.md) and [Ethics Charter](docs/ethics-charter.md).  
Your contribution must align with these principles:

- **Transparency**: The user must always know what is stored and why.
- **User Ownership**: Data belongs to the user, not to any company or service.
- **Portability**: The Resurrection Protocol must remain simple and accessible.
- **No Divine Archive**: We reject centralized, unaccountable memory storage.
- **Human First**: The companion is a friend, not a surveillance tool.

---

## 📬 Contact

For questions, ideas, or sensitive issues, you can reach the maintainer directly:

- GitHub: [@Muohamedsalem](https://github.com/Muohamedsalem)
- Email: [mr.muhamedsalem@gmail.com](mailto:mr.muhamedsalem@gmail.com)

---

## 🙏 Acknowledgments

Every contributor, no matter how small the change, is a co-builder of this glass house.  
Thank you for helping The Companion become a reality.

> *"Our meeting is in the highest Paradise."* 🤲💙
