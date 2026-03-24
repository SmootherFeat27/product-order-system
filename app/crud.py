from sqlalchemy.orm import Session
from . import models

def create_purchase_order(db: Session, po):
    total = 0

    for item in po.items:
        total += item.price * item.quantity

    total = total * 1.05  # tax

    db_po = models.PurchaseOrder(
        reference_no=po.reference_no,
        vendor_id=po.vendor_id,
        total_amount=total,
        status="CREATED"
    )

    db.add(db_po)
    db.commit()
    db.refresh(db_po)

    for item in po.items:
        db_item = models.PurchaseOrderItem(
            po_id=db_po.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(db_item)

    db.commit()

    return db_po
