# Composer

https://docs.cursor.com/composer/overview

Cursor AI offers two distinct interfaces—**Chat** and **Composer**—each designed to serve different parts of your coding workflow.

---

### Chat

**Purpose & Capabilities:**  
• **Code Exploration and Debugging:**  
 – Chat is primarily used to ask questions about your code, understand its behavior, or troubleshoot issues. It works in the context of the current file and cursor position, making it great for quick queries and getting insights or explanations.  
 – When Chat provides code suggestions or fixes, you typically review them and then apply the changes manually.  

**How to Use Chat:**  
• **Activation:**  
 – Use the shortcut (usually **Ctrl + L** on Windows or the equivalent on macOS) to open the Chat panel.  
• **Workflow:**  
 – Type your question or describe what you need help with (for example, debugging an issue or understanding a code segment).  
 – Review the response, which might include explanations or code snippets.  
 – Manually apply any suggested changes to your code as needed.

*Reference:* Community feedback on Cursor forums notes that Chat is intended for in-file queries and understanding code without auto-applying changes.

---

### Composer

**Purpose & Capabilities:**  
• **Extensive Code Modification:**  
 – Composer is built for writing and editing code across multiple files. It can generate new code, create files and directories, and even refactor code automatically.  
 – It provides a diff view that lets you review proposed changes before they’re applied, which is especially useful for larger, multi-file edits.  
 – Composer is known for its “auto-apply” nature: once you review the changes, you can accept them with a single click, streamlining your workflow.

**How to Use Composer:**  
• **Activation:**  
 – Open Composer with **Ctrl + I** (or **Cmd + I** on macOS) to launch a floating window, sidebar pane, or control panel view.  
• **Workflow:**  
 – Enter your instruction for modifying the code—this could be a request to refactor, add features, or generate new code.  
 – Review the diff view of the changes proposed by Composer.  
 – Accept (or reject) the changes using the provided buttons, which will update your code across one or more files.

*Reference:* The official Cursor documentation and community discussions emphasize that Composer is geared toward multi-file edits and direct code modifications.

---

### Summary

- **Chat** is best when you need to **ask questions, debug, or understand your existing code**. It leverages your current context but requires manual intervention to update your code.
  
- **Composer** is ideal when you want to **perform extensive modifications**, refactor code, or generate new code across multiple files. It provides a structured workspace that automatically applies changes after review.

By choosing Chat for quick, on-the-fly assistance and Composer for comprehensive, multi-file code editing, you can tailor your workflow to fit your development needs and make the most of Cursor AI’s capabilities.

In short, if your window shows an editing workspace with a diff view and clear “apply” options, you’re in Composer. If it’s a simpler chat interface meant for asking questions and getting explanations without directly modifying your code, then you’re in Chat.


